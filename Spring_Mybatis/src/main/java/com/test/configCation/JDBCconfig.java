package com.test.configCation;

import com.alibaba.druid.pool.DruidDataSource;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;

import javax.sql.DataSource;

//@PropertySource("classpath:jdbc.properties")//加载 jdbc配置文件
public class JDBCconfig {
    @Value("${driver}")
    private String driver;
    @Value("${url}")
    private String url;
    @Value("${username}")
    private String userName;
    @Value("${password}")
    private String passWord;
    @Bean
    public DataSource dataSource(){
//        System.out.println(name);
        DruidDataSource druid = new DruidDataSource();
        druid.setDriverClassName(driver);
        druid.setUrl(url);
        druid.setUsername(userName);
        druid.setPassword(passWord);
        return druid;
    }
}
