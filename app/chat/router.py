from uuid import UUID

from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import Response

from app.chat.schemas import TextChatRequest, TextChatResponse, VoiceChatResponse
from app.chat.service import process_text_chat, process_voice_chat
from app.dependencies import CurrentUser, DbSession

router = APIRouter()


@router.post("/text", response_model=TextChatResponse)
async def text_chat(db: DbSession, current_user: CurrentUser, request: TextChatRequest):
    """
    Send a text message and receive a text response.
    """
    return await process_text_chat(db, current_user.id, request)


@router.post("/voice", response_model=VoiceChatResponse)
async def voice_chat(
    db: DbSession,
    current_user: CurrentUser,
    conversation_id: UUID = Form(...),
    audio: UploadFile = File(...),
):
    """
    Send a voice message and receive a text response.

    The audio file should be in a supported format (wav, mp3, webm, etc.)
    """
    audio_data = await audio.read()
    response, _ = await process_voice_chat(db, current_user.id, conversation_id, audio_data)
    return response


@router.post("/voice/audio")
async def voice_chat_with_audio(
    db: DbSession,
    current_user: CurrentUser,
    conversation_id: UUID = Form(...),
    audio: UploadFile = File(...),
):
    """
    Send a voice message and receive an audio response.

    Returns the audio response directly as bytes.
    """
    audio_data = await audio.read()
    _, audio_response = await process_voice_chat(db, current_user.id, conversation_id, audio_data)

    if audio_response:
        return Response(content=audio_response, media_type="audio/mpeg")
    return Response(status_code=204)
