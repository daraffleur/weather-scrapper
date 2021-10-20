import requests
from bs4 import BeautifulSoup

from rest_framework.views import APIView
from rest_framework.response import Response

from crud.serializers import WeatherSerializer


class WeatherScrapperView(APIView):
    def get(self, request):
        page = requests.get("https://www.bbc.com/weather/1275339")
        soup = BeautifulSoup(page.text, "html.parser")

        weather_data = soup.find(class_="wr-day-carousel__scrollable")
        days = weather_data.find_all("li")

        weather_results = []
        for d in days:
            day = d.find(class_="wr-date").get_text()
            description = d.find(
                class_="wr-day__weather-type-description-container"
            ).get_text()
            temperature = d.find(class_="wr-day-temperature").get_text()
            weather_info_per_day = {
                "day": day,
                "description": description,
                "temperature": temperature,
            }
            weather_results.append(weather_info_per_day)
        results = WeatherSerializer(
            weather_results,
            many=True,
        ).data
        return Response(results)
