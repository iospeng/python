package com.test;

import com.test.configCation.SpringConfig;
import com.test.domain.Account;
import com.test.service.AccountService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class app {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(SpringConfig.class);
        AccountService bean = ctx.getBean(AccountService.class);
        Account account = bean.findById(1);
        System.out.println(account);
    }
}
