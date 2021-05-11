from enum import Enum, auto

class Welcomedata_type(Enum):
    text = auto()
    sticker = auto()
    animation= auto()
    document = auto()
    photo = auto()
    audio = auto()
    voice = auto()
    video = auto()
    video_note = auto()


def GetWelcomeMessage(message):
    data_type = None
    content = None
    text = str()

    if not (
        message.reply_to_message
    ):
        content = None
        text = message.text.markdown[len(message.command[0]) + 2 :]
        data_type = Welcomedata_type.text.value

    elif (
        message.reply_to_message
        and message.reply_to_message.text
    ):
        content = None
        text = message.reply_to_message.text.markdown 
        data_type = Welcomedata_type.text.value

    elif (
        message.reply_to_message
        and message.reply_to_message.sticker
    ):
        content = message.reply_to_message.sticker.file_id
        data_type = Welcomedata_type.sticker.file_id
    
    elif (
        message.reply_to_message
        and message.reply_to_message.animation
    ):
        content = message.reply_to_message.animation.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = FilterMessageTypeMap.animation.value

    elif (
        message.reply_to_message
        and message.reply_to_message.document
    ):
        content = message.reply_to_message.document.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type = Welcomedata_type.document.value

    elif (
        message.reply_to_message
        and message.reply_to_message.photo
    ):
        content = message.reply_to_message.photo.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = Welcomedata_type.photo.value

    elif (
        message.reply_to_message
        and message.reply_to_message.audio
    ):
        content = message.reply_to_message.audio.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type = Welcomedata_type.audio.value

    elif (
        message.reply_to_message
        and message.reply_to_message.voice
    ):
        content = message.reply_to_message.voice.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type = Welcomedata_type.voice.value

    elif (
        message.reply_to_message
        and message.reply_to_message.video
    ):
        content = message.reply_to_message.video.file_id 
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type= Welcomedata_type.video.value

    elif (
        message.reply_to_message
        and message.reply_to_message.video_note
    ):
        content = message.reply_to_message.video_note.file_id
        text = None 
        data_type = Welcomedata_type.video_note.value
    
    return (
        content,
        text,
        data_type
    )