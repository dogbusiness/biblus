curl -X PUT "localhost:5601/book" -H 'Content-Type: application/json' -d' {
      "mappings": {
        "properties": {
          "title": { "type": "text" },
          "author": { "type": "text" },
          "year": {"type": "date"},
          "pages": {"type": "integer"},
          "size": { "type": "text" },
          "published_by": { "type": "text" },
          "description": { "type": "text" },
          "cover": { "type": "text" },
          "download_links": {"properties": {"extension": { "type": "keyword" }}},
          "tor_link": {"type": "keyword"},
          "link_upd_by": {"type": "date"}
        }
      }
    }
    '
