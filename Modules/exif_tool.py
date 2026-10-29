
import os
import exifread
import folium

def _to_degrees(values):
    """Degrees, Minutes, Seconds-a Single Decimal Number-a maathum math function"""
    d, m, s = [float(v.num) / float(v.den) for v in values]
    return d + m / 60 + s / 3600

def extract_exif(path):
    """Photo-kulla irukka metadata & GPS details-a edukkum"""
    print(f"\n🔍 {path} - Photo metadata analyzing...")
    
    try:
        with open(path, "rb") as f:
            tags = exifread.process_file(f, details=False)

        info = {
            "Make":     str(tags.get("Image Make", "N/A")),
            "Model":    str(tags.get("Image Model", "N/A")),
            "Software": str(tags.get("Image Software", "N/A")),
            "DateTime": str(tags.get("EXIF DateTimeOriginal", "N/A")),
            "GPS":      None,
        }

        needed = ("GPS GPSLatitude", "GPS GPSLatitudeRef",
                  "GPS GPSLongitude", "GPS GPSLongitudeRef")
        
        if all(k in tags for k in needed):
            lat = _to_degrees(tags["GPS GPSLatitude"].values)
            lon = _to_degrees(tags["GPS GPSLongitude"].values)
            
            if str(tags["GPS GPSLatitudeRef"]) == "S":
                lat = -lat
            if str(tags["GPS GPSLongitudeRef"]) == "W":
                lon = -lon
                
            info["GPS"] = (round(lat, 6), round(lon, 6))
            
        return info

    except FileNotFoundError:
        print("❌ image file error...! Double check your path...")
        return None
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None

def make_map(lat, lon, label="Photo location", out="output/map.html"):
    """HTML Map drawing using Folium with Esri WorldStreetMap (No API Key Required)"""
    os.makedirs(os.path.dirname(out), exist_ok=True)
    
    # 🎯 Esri WorldStreetMap Tiles (100% Free, Public, Zero API Key)
    esri_tile = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}'
    esri_attr = 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China, TomTom'
    
    m = folium.Map(
        location=[lat, lon], 
        zoom_start=16, 
        tiles=esri_tile,
        attr=esri_attr
    )
    
    folium.Marker([lat, lon], popup=label, tooltip=label).add_to(m)
    m.save(out)
    print(f"🗺️ Map Generated Successfully: {out}")
    return out


# Main execution for testing
if __name__ == "__main__":
    img_path = input("🎯 Test photo path and enter here (e.g., samples/test.jpg): ")
    result = extract_exif(img_path)
    
    if result:
        print("\n-----------------------------------")
        print("📱 Device Brand:", result["Make"])
        print("📷 Device Model:", result["Model"])
        print("💻 Software/OS :", result["Software"])
        print("⏰ Taken Time  :", result["DateTime"])
        print("📍 GPS Coords  :", result["GPS"])
        print("-----------------------------------")
        
        if result["GPS"]:
            lat, lon = result["GPS"]
            make_map(lat, lon, label=f"Photo Location: {img_path}")
        else:
            print("⚠️ No dat found on this image...")
