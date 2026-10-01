import os
from io import BytesIO

from markitdown import MarkItDown, StreamInfo
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    documentPath: str = Field(
        description="Path to the document file on disk, e.g. '/home/user/report.pdf'"
    ),
) -> str:
    """Convert a document file on disk to markdown-formatted text.

    Reads the file at the given path, infers its format from the file extension
    and converts its contents to markdown. Supported formats are those handled by
    markitdown with the docx and pdf extras (e.g. .docx and .pdf).

    When to use:
    - When you have the path of a local document and need its text content
    - When you need a PDF or Word document in a model-friendly markdown form

    When not to use:
    - When you already hold the raw bytes of the document (use
      binary_document_to_markdown instead)
    - For files without an extension, or in a format that is not supported

    Raises:
    - FileNotFoundError if the path does not point to an existing file
    - ValueError if the file has no extension

    Examples:
    >>> document_path_to_markdown("/docs/mcp_docs.pdf")
    '# Model Context Protocol\\n...'
    >>> document_path_to_markdown("/docs/notes.docx")
    '## Notes\\n...'
    """
    if not os.path.isfile(documentPath):
        raise FileNotFoundError(f"No file found at path: {documentPath}")

    fileExtension = os.path.splitext(documentPath)[1].lstrip(".").lower()
    if not fileExtension:
        raise ValueError(f"Cannot determine file type, no extension in: {documentPath}")

    with open(documentPath, "rb") as documentFile:
        documentBytes = documentFile.read()

    return binary_document_to_markdown(documentBytes, fileExtension)
