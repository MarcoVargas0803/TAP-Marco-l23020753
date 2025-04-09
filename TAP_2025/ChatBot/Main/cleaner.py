import re

def clean_corpus(chat_export_file):
    """Prepare a WhatsApp chat export for training with chatterbot."""
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus

def remove_chat_metadata(chat_export_file):
    """Remove WhatsApp chat metadata.

    WhatsApp chat exports come with metadata about each message:

     date    time    username  message
    ---------------------------------------
    8/26/22, 17:47 - Jane Doe: Message text

    This function removes all the metadata up to the text of each message.

    Args:
        chat_export_file (str): The name of the chat export file

    Returns:
        tuple: The text of each message in the conversation
    """
    date_time = r"\[\d{2}/\d{2}/\d{2},\s\d{2}:\d{2}:\d{2}\s?(a\.m\.|p\.m\.)\]"  # [dd/mm/aa, hh:mm:ss a.m./p.m.] Nombre:
    username = r"\s.+?:\s"  # Nombre de usuario con cualquier carácter hasta los dos puntos
    metadata_end = r":\s"  # ": "
    pattern = date_time + username + metadata_end

    with open(chat_export_file, "r", encoding="utf-8") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    """
    Elimina texto irrelevante de la exportación de chats de WhatsApp,
    como medios omitidos, enlaces y mensajes de error.
    """
    # Puedes ajustar estos términos si hay otros en tus chats
    media_indicators = (
        "sticker omitted",
        "image omitted",
        "video omitted",
        "audio omitted",
        "document omitted",
        "GIF omitted",
        "contact card omitted",
        "Messages and calls are end-to-end encrypted.",
        "Waiting for this message. This may take a while.",
        "<Media omitted>",
    )

    cleaned_messages = []

    for line in export_text_lines[1:-1]:  # Saltamos línea inicial y final

        # Quitar espacios invisibles Unicode como el carácter de dirección (LTR/RTL)
        line = line.replace('\u200e', '').strip()

        # Ignorar si contiene alguno de los textos a eliminar
        if any(indicator.lower() in line.lower() for indicator in media_indicators):
            continue

        # Ignorar si contiene un enlace
        if re.search(r"https?://\S+", line):
            continue

        # Ignorar líneas vacías
        if not line.strip():
            continue

        cleaned_messages.append(line)

    return tuple(cleaned_messages)
