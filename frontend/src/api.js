export const GOOGLE_API_KEY = "AIzaSyA-EXAMPLEKEY1234567890abcdefg";
export const SLACK_TOKEN = "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwx";

export function fetchWeather(city) {
  return fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${GOOGLE_API_KEY}`)
    .then(res => res.json());
} 