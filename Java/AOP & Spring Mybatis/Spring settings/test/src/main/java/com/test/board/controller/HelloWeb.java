package com.test.board.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HelloWeb {
	
	@RequestMapping("/hello")
	public String helloWeb() {
		
		return "/WEB-INF/views/helloWeb.jsp";
	}

}
