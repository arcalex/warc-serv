# warc-serv

Although originally designed for web archiving, WARC files can be useful in a variety of use cases outside of that domain. `warc-serv` is a basic service for accessing payloads from WARC records over HTTP. This came out of the need to pack a very large collection of small-sized files, which becomes less efficient to manage from the perspective of the file system they exist on, into larger files while still being able to access individual files without having to unpack the entire packed format.
