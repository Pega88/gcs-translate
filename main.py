from google.cloud import translate_v3


def translate_document(
    input_path: str,
    output_path: str,
    project_id: str,
    location: str,
    target_language: str,
) -> translate_v3.TranslationServiceClient:


    client = translate_v3.TranslationServiceClient()
    parent = f"projects/{project_id}/locations/{location}"


    document_input_config = translate_v3.DocumentInputConfig()
    document_input_config.gcs_source.input_uri = input_path
    document_input_config.mime_type = "application/pdf"


    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": target_language,
            "document_input_config": document_input_config,
        }
    )

    f = open(output_path, 'wb')
    f.write(response.document_translation.byte_stream_outputs[0])
    f.close()

    print(
        f"File saved to: {output_path}. Detected Language Code was {response.document_translation.detected_language_code}"
    )

    return response

translate_document("gs://my-gcs-bucket/file.pdf","/Users/johndoe/Documents/test.pdf","my-project","us-central1","en")
