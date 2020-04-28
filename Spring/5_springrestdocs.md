[TOC]

------

### build.gradle

```groovy
plugins {
    ...
	id "org.asciidoctor.convert" version "1.5.8"
    ...
}

bootJar {
	dependsOn asciidoctor
	from ("${asciidoctor.outputDir}/html5") {
		into 'static/docs'
	}
}
ext {
	set('snippetsDir', file("build/generated-snippets"))
}


dependencies {
    
	...

	// spring rest docs
	testImplementation 'org.springframework.restdocs:spring-restdocs-mockmvc'
	asciidoctor 'org.springframework.restdocs:spring-restdocs-asciidoctor'
}
```

<br>

### Common

```java
package com.webatoz.backend.interfaces.global;

import org.json.JSONObject;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.hateoas.MediaTypes;
import org.springframework.restdocs.RestDocumentationContextProvider;
import org.springframework.restdocs.RestDocumentationExtension;
import org.springframework.restdocs.hypermedia.LinkDescriptor;
import org.springframework.restdocs.hypermedia.LinksSnippet;
import org.springframework.restdocs.mockmvc.RestDocumentationResultHandler;
import org.springframework.restdocs.payload.FieldDescriptor;
import org.springframework.restdocs.payload.ResponseFieldsSnippet;
import org.springframework.restdocs.request.ParameterDescriptor;
import org.springframework.restdocs.request.RequestParametersSnippet;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.springframework.restdocs.hypermedia.HypermediaDocumentation.linkWithRel;
import static org.springframework.restdocs.hypermedia.HypermediaDocumentation.links;
import static org.springframework.restdocs.mockmvc.MockMvcRestDocumentation.document;
import static org.springframework.restdocs.mockmvc.MockMvcRestDocumentation.documentationConfiguration;
import static org.springframework.restdocs.mockmvc.RestDocumentationRequestBuilders.*;
import static org.springframework.restdocs.operation.preprocess.Preprocessors.prettyPrint;
import static org.springframework.restdocs.payload.PayloadDocumentation.fieldWithPath;
import static org.springframework.restdocs.payload.PayloadDocumentation.relaxedResponseFields;
import static org.springframework.restdocs.request.RequestDocumentation.parameterWithName;
import static org.springframework.restdocs.request.RequestDocumentation.requestParameters;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;

@SpringBootTest
@ExtendWith({ RestDocumentationExtension.class, SpringExtension.class })
@ActiveProfiles("local")
public class CommonDocumentationTests {

    private RestDocumentationResultHandler documentationHandler;
    private MockMvc mockMvc;

    @BeforeEach
    public void setUp(WebApplicationContext webApplicationContext, RestDocumentationContextProvider restDocumentation) {
        this.documentationHandler = document("{method-name}");
        this.mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext)
                .apply(
                        documentationConfiguration(restDocumentation)
                                .uris()
                                .withScheme("https")
                                .withHost("webatoz.com")
                                .withPort(443)
                        .and()
                                .operationPreprocessors()
                                .withRequestDefaults(prettyPrint())
                                .withResponseDefaults(prettyPrint())
                )
                .alwaysDo(documentationHandler)
                .alwaysDo(print())
                .build();
    }

    // return ResultActions on request method
    protected ResultActions postAction(JSONObject requestData, String urlTemplate, Object... urlVariables) throws Exception {
        return this.mockMvc.perform(post(urlTemplate, urlVariables)
                .contentType(MediaTypes.HAL_JSON)
                .content(requestData.toString())
        );
    }
    protected ResultActions putAction(JSONObject requestData, String urlTemplate, Object... urlVariables) throws Exception {
        return this.mockMvc.perform(put(urlTemplate, urlVariables)
                .contentType(MediaTypes.HAL_JSON)
                .content(requestData.toString())
        );
    }
    protected ResultActions getAction(String urlTemplate, Object... urlVariables) throws Exception {
        return this.mockMvc.perform(get(urlTemplate, urlVariables)
                .contentType(MediaTypes.HAL_JSON)
        );
    }
    protected ResultActions deleteAction(String urlTemplate, Object... urlVariables) throws Exception {
        return this.mockMvc.perform(delete(urlTemplate, urlVariables)
                .contentType(MediaTypes.HAL_JSON)
        );
    }
}

```

<br>

### BoardController

```java
package com.webatoz.backend.interfaces.board;

import com.webatoz.backend.interfaces.global.CommonDocumentationTests;
import org.junit.jupiter.api.Test;
import org.springframework.restdocs.payload.JsonFieldType;

import static org.springframework.restdocs.hypermedia.HypermediaDocumentation.linkWithRel;
import static org.springframework.restdocs.hypermedia.HypermediaDocumentation.links;
import static org.springframework.restdocs.mockmvc.MockMvcRestDocumentation.document;
import static org.springframework.restdocs.payload.PayloadDocumentation.fieldWithPath;
import static org.springframework.restdocs.payload.PayloadDocumentation.relaxedResponseFields;
import static org.springframework.restdocs.request.RequestDocumentation.parameterWithName;
import static org.springframework.restdocs.request.RequestDocumentation.requestParameters;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

class BoardController extends CommonDocumentationTests {

    @Test
    void getBoards() throws Exception {
        getAction("/boards")
                .andExpect(status().isOk()) // 다른 검증 추가
                .andDo(document("{method-name}",
                        requestParameters(
                                parameterWithName("page").description("The page to retrieve (default=1)").optional(),
                                parameterWithName("size").description("Entries per page (default=20)").optional()
                        ),
                        links(
                                linkWithRel("self").description("link to self"),
                                linkWithRel("profile").description("document link"),
                                linkWithRel("first").description("The first page of results").optional(),
                                linkWithRel("prev").description("The previous page of results").optional(),
                                linkWithRel("next").description("The next page of results").optional(),
                                linkWithRel("last").description("The last page of results").optional()
                        ),
                        relaxedResponseFields(
                                fieldWithPath("code").type(JsonFieldType.STRING).description("result code"),
                                fieldWithPath("message").type(JsonFieldType.STRING).description("result message"),
                                fieldWithPath("_embedded.boards[]").type(JsonFieldType.ARRAY).description("list of board"),
                                fieldWithPath("_embedded.boards[].id").type(JsonFieldType.NUMBER).description("board id"),
                                fieldWithPath("_embedded.boards[].title").type(JsonFieldType.STRING).description("board title"),
                                fieldWithPath("_embedded.boards[].createdDate").type(JsonFieldType.STRING).description("created date"),
                                fieldWithPath("_embedded.boards[].updatedDate").type(JsonFieldType.STRING).description("updated date"),
                                fieldWithPath("_embedded.boards[].deletedDate").type(JsonFieldType.STRING).description("deleted date")
                        )
                ));
    }

}
```



테스트 코드를 실행하고 스프링 부트를 실행 이후 http://localhost:8080/docs/api-guide.html를 접속하면 Rest Docs 기반의 문서를 확인 할 수 있습니다.

