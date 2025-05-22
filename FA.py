from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Annotated
from utils import send_data_to_chanel_file


from Bot import bot
import uvicorn
app = FastAPI()


@app.post("/upload")
async def upload_photo_and_text(
    photo: Annotated[UploadFile, File(description="Загружаемое фото")],
    text: Annotated[str, Form(description="Текстовая информация")],
    user_id: Annotated[int, Form(description="Id человека")]
):
    print("dfs")
    # Сохраняем фото на сервер
    photo = await photo.read()
    await send_data_to_chanel_file(bot=bot, text=text, user_id=user_id, photo=photo)

    # Возвращаем информацию о загруженных данных
    return JSONResponse(
        status_code=200,
        content={
            "message": "Фото и текст успешно получены!",
            "filename": "photo.filename",
            "content_type": "photo.content_type",
            "text": text,
            "saved_path": "t",
        },
    )

if __name__ == "__main__":
    print(1234)
    uvicorn.run(app, host="0.0.0.0", port=80)
