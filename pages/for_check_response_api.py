class Map:
    schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "zoom_1": {
      "type": "object",
      "properties": {
        "minmax": {
          "type": "object",
          "properties": {
            "curr_scipub_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_niokr_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_rid_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_diss_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_grant_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_patent_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_summary": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 }
          },
          "required": [
            "curr_scipub_count",
            "curr_niokr_count",
            "curr_rid_count",
            "curr_diss_count",
            "curr_grant_count",
            "curr_patent_count",
            "curr_summary"
          ]
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "curr_scipub_count": { "type": "integer" },
              "curr_niokr_count": { "type": "integer" },
              "curr_rid_count": { "type": "integer" },
              "curr_diss_count": { "type": "integer" },
              "curr_grant_count": { "type": "integer" },
              "curr_patent_count": { "type": "integer" },
              "curr_usu_count": { "type": "integer" },
              "curr_ckp_count": { "type": "integer" },
              "curr_ikrbs_count": { "type": "integer" },
              "curr_summary": { "type": "integer" },
              "count_orgs": { "type": "integer" },
              "object": {
                "type": "object",
                "properties": {
                  "type_map_obj": { "type": "string" },
                  "uid": { "type": "string" }
                },
                "required": ["type_map_obj", "uid"]
              },
              "name": { "type": "string" },
              "NAME_1": { "type": "string" },
              "ID_1": { "type": "string" }
            },
            "required": [
              "curr_scipub_count",
              "curr_niokr_count",
              "curr_rid_count",
              "curr_diss_count",
              "curr_grant_count",
              "curr_patent_count",
              "curr_usu_count",
              "curr_ckp_count",
              "curr_ikrbs_count",
              "curr_summary",
              "count_orgs",
              "object",
              "name",
              "NAME_1",
              "ID_1"
            ]
          }
        },
        "cities": { "type": "array", "items": { "type": "string" } },
        "cities_add": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "uid": { "type": "string" },
              "title": { "type": "string" },
              "longitude": { "type": "number" },
              "latitude": { "type": "number" }
            },
            "required": ["uid", "title", "longitude", "latitude"]
          }
        }
      },
      "required": ["minmax", "data", "cities", "cities_add"]
    },
    "zoom_2": {
      "type": "object",
      "properties": {
        "minmax": {
          "type": "object",
          "properties": {
            "curr_scipub_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_niokr_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_rid_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_diss_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_grant_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_patent_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_summary": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 }
          },
          "required": [
            "curr_scipub_count",
            "curr_niokr_count",
            "curr_rid_count",
            "curr_diss_count",
            "curr_grant_count",
            "curr_patent_count",
            "curr_summary"
          ]
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "curr_scipub_count": { "type": "integer" },
              "curr_niokr_count": { "type": "integer" },
              "curr_rid_count": { "type": "integer" },
              "curr_diss_count": { "type": "integer" },
              "curr_grant_count": { "type": "integer" },
              "curr_patent_count": { "type": "integer" },
              "curr_usu_count": { "type": "integer" },
              "curr_ckp_count": { "type": "integer" },
              "curr_ikrbs_count": { "type": "integer" },
              "curr_summary": { "type": "integer" },
              "count_orgs": { "type": "integer" },
              "lon": { "type": "number" },
              "lat": { "type": "number" },
              "status_city": { "type": "boolean" },
              "object": {
                "type": "object",
                "properties": {
                  "type_map_obj": { "type": "string" },
                  "uid": { "type": "string" }
                },
                "required": ["type_map_obj", "uid"]
              },
              "name": { "type": "string" },
              "last_city": { "type": "string" }
            },
            "required": [
              "curr_scipub_count",
              "curr_niokr_count",
              "curr_rid_count",
              "curr_diss_count",
              "curr_grant_count",
              "curr_patent_count",
              "curr_usu_count",
              "curr_ckp_count",
              "curr_ikrbs_count",
              "curr_summary",
              "count_orgs",
              "lon",
              "lat",
              "status_city",
              "object",
              "name",
              "last_city"
            ]
          }
        },
        "cities": { "type": "array", "items": { "type": "string" } },
        "cities_add": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "uid": { "type": "string" },
              "title": { "type": "string" },
              "longitude": { "type": "number" },
              "latitude": { "type": "number" }
            },
            "required": ["uid", "title", "longitude", "latitude"]
          }
        }
      },
      "required": ["minmax", "data", "cities", "cities_add"]
    },
    "zoom_3": {
      "type": "object",
      "properties": {
        "minmax": {
          "type": "object",
          "properties": {
            "curr_scipub_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_niokr_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_rid_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_diss_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_grant_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_patent_count": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
            "curr_summary": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 }
          },
          "required": [
            "curr_scipub_count",
            "curr_niokr_count",
            "curr_rid_count",
            "curr_diss_count",
            "curr_grant_count",
            "curr_patent_count",
            "curr_summary"
          ]
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "curr_scipub_count": { "type": "integer" },
              "curr_niokr_count": { "type": "integer" },
              "curr_rid_count": { "type": "integer" },
              "curr_diss_count": { "type": "integer" },
              "curr_grant_count": { "type": "integer" },
              "curr_patent_count": { "type": "integer" },
              "curr_usu_count": { "type": "integer" },
              "curr_ckp_count": { "type": "integer" },
              "curr_ikrbs_count": { "type": "integer" },
              "curr_summary": { "type": "integer" },
              "count_orgs": { "type": "integer" },
              "lon": { "type": "number" },
              "lat": { "type": "number" },
              "object": {
                "type": "object",
                "properties": {
                  "type_map_obj": { "type": "string" },
                  "uid": { "type": "string" }
                },
                "required": ["type_map_obj", "uid"]
              },
              "name": { "type": "string" }
            },
            "required": [
              "curr_scipub_count",
              "curr_niokr_count",
              "curr_rid_count",
              "curr_diss_count",
              "curr_grant_count",
              "curr_patent_count",
              "curr_usu_count",
              "curr_ckp_count",
              "curr_ikrbs_count",
              "curr_summary",
              "count_orgs",
              "lon",
              "lat",
              "object",
              "name"
            ]
          }
        },
        "cities": { "type": "array", "items": { "type": "string" } },
        "cities_add": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "uid": { "type": "string" },
              "title": { "type": "string" },
              "longitude": { "type": "number" },
              "latitude": { "type": "number" }
            },
            "required": ["uid", "title", "longitude", "latitude"]
          }
        }
      },
      "required": ["minmax", "data", "cities", "cities_add"]
    }
  },
  "required": ["zoom_1", "zoom_2", "zoom_3"]
}


class Statistic:
  schema = {
    "results": [
      {
        "chart_type_name": "string",
        "chart_uid": "string",
        "type": "string",
        "data": {
          "labels": [
            "number"
          ],
          "datasets": [
            {
              "label": [
                "string"
              ],
              "data": [
                "number"
              ],
              "backgroundColor": "string",
              "type": "string"
            }
          ]
        },
        "options": {
          "plugins": {
            "title": {
              "display": "boolean",
              "text": "string"
            },
            "responsive": "boolean",
            "legend": {
              "display": "boolean",
              "position": "string",
              "labels": {
                "positionStyle": "string"
              }
            }
          },
          "scales": {
            "x": {
              "stacked": "boolean",
              "title": {
                "display": "boolean",
                "text": "string"
              }
            },
            "y": {
              "stacked": "boolean",
              "title": {
                "display": "boolean",
                "text": "string"
              }
            }
          }
        }
      }
    ],
    "error": [
      None,
      "string"
    ]
  }
