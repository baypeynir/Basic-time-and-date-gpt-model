import requests
from datetime import datetime
from pytz import timezone
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Buraya kendi OpenWeatherMap API anahtarınızı girin

def get_timezone_info(city: str):
    try:
        geolocator = Nominatim(user_agent="wgpt")
        location = geolocator.geocode(city)
        if not location:
            print("Şehir bulunamadı.")
            return None, None

        tf = TimezoneFinder()
        tz_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
        if not tz_str:
            print("Zaman dilimi bulunamadı.")
            return None, None

        local_time = datetime.now(timezone(tz_str))
        return tz_str, local_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Zaman bilgisi alınamadı: {e}")
        return None, None

def main():
    city = input("Şehir veya yer ismi girin: ").strip()

    tz, local_time = get_timezone_info(city)
    if tz and local_time:
        print(f"\n📍 {city} için bilgiler:")
        print(f"🕒 Yerel saat: {local_time} ({tz})")

        

if __name__ == "__main__":
    main()
