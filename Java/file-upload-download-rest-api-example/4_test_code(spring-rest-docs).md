[TOC]

### upload

```java
@Test
void uploadFile() throws Exception {
    MockMultipartFile file = new MockMultipartFile("file", "test.txt", "text/plain", "hello file".getBytes());

    this.mockMvc.perform(MockMvcRequestBuilders.multipart("/admin/upload-file")
                         .file(file)
                        )
        .andDo(print())
        .andExpect(status().isCreated())
        .andDo(document("admin-upload-file",
                        requestParts(
                            partWithName("file").description("The file to upload")
                        ),
                        relaxedResponseFields(
                            fieldWithPath("code").description("result code"),
                            fieldWithPath("message").description("result message"),
                            fieldWithPath("_embedded.file").description("upload file info data"),
                            fieldWithPath("_embedded.file.fileName").description("file name").type(JsonFieldType.STRING),
                            fieldWithPath("_embedded.file.fileDownloadUri").description("file download URI").type(JsonFieldType.STRING),
                            fieldWithPath("_embedded.file.fileType").description("file type").type(JsonFieldType.STRING),
                            fieldWithPath("_embedded.file.size").description("size").type(JsonFieldType.NUMBER)
                        )
                       ));
}
```

<br>

### get

```java
@Test
void getFile() throws Exception {
    getAction("/file/test.txt")
        .andExpect(status().isOk())
        .andDo(print())
        .andDo(document("get-file"));
}

@Test
void getVideoStream() throws Exception {
    this.mockMvc.perform(get("/{name}", "01-test.mp4")
                         .contentType(MediaType.APPLICATION_JSON)
                         .accept("application/hal+json;charset=UTF-8")
                         .header(Header.AUTH.getValue(), "****")
                         .header("Range", "bytes=14385152-22008564")
                        )
        .andExpect(status().isPartialContent())
        .andDo(print())
        .andDo(document("get-video",
                        requestHeaders(headerWithName("Range").description("range")))
              );
}
```

