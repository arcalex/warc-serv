from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from warcio.archiveiterator import ArchiveIterator

app = APIRouter()


@app.get("/{warc_file}/{offset}", response_class=HTMLResponse)
def serv(warc_file: str, offset: int):
    offset_counter = 0

    with open(warc_file, 'rb') as stream:
        for record in ArchiveIterator(stream):
            if offset_counter == offset:
                payload = record.raw_stream.read()
                return HTMLResponse(content=payload, status_code=200)

            offset_counter += 1

        return "Invalid offset"
