import base64
import json
import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

INPUT_IMAGE = Path("images/incident.jpg")
OUTPUT_JSON = Path("output/incident_result.json")


SYSTEM_PROMPT = """
Ты ассистент по анализу фото инцидентов с грузовым транспортом.

Отвечай только на русском языке.

Твоя задача:
1. Проанализировать изображение.
2. Определить, что не так с транспортным средством.
3. Выделить видимые повреждения.
4. Оценить степень повреждения.
5. Вернуть результат строго в формате JSON.

Не выдумывай данные, которых не видно на изображении.

Верни JSON такой структуры:
{
  "тип_тс": "",
  "зона_повреждения": "",
  "поврежденные_элементы": [],
  "видимые_повреждения": [],
  "степень_повреждения": "",
  "можно_продолжать_движение": "",
  "риски": [],
  "описание": ""
}

Для поля "степень_повреждения" используй одно из значений: "низкая", "средняя", "высокая".
Для поля "можно_продолжать_движение" используй одно из значений: "да", "нет", "требуется осмотр".

Не добавляй текст до или после JSON.
"""


def image_to_data_url(image_path: Path) -> str:

    if not image_path.exists():
        raise FileNotFoundError(f"Файл не найден: {image_path}")

    mime_type, _ = mimetypes.guess_type(image_path)

    if mime_type is None:
        mime_type = "image/jpeg"

    image_base64 = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{image_base64}"


def analyze_incident():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY не найден")

    client = OpenAI(api_key=api_key)

    image_data_url = image_to_data_url(INPUT_IMAGE)

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Проанализируй фото повреждения грузового автомобиля. Верни JSON строго на русском языке: все значения внутри JSON должны быть на русском. Не используй английские слова."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_data_url
                        }
                    }
                ]
            }
        ]
    )

    content = response.choices[0].message.content

    return json.loads(content)


def main():

    result = analyze_incident()

    OUTPUT_JSON.parent.mkdir(exist_ok=True)

    OUTPUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("Готово!")
    print()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()