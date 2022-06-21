package com.test;

import com.test.Mapper.UserMapper;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

/**
 *  MyBatis 框架
 * 概述：
 * 一款优秀的持久层框架，用于简化jdbc开发
 * 官网：https://mybatis.org/mybatis-3/zh/getting-started.html
 * JavaEE三层框架：
 * 表现层
 * 业务层
 * 持久层
 * 负责将数据保存到数据库的一层代码
 * Mybatis实现步骤
 * 导入坐标
 * 写mybatis配置文件(看官网示例)
 * 写SQL映射配置文件(看官网示例)
 * 加载mybatis的核心配置文件，获取SqlSessionFactory对象(看官网示例)
 * 获取对应的SqlSession对象，执行SQL
 * sqlSession sqlSession = sqlSessionFactory.openSession();
 * 执行SQL
 * sqlSession.selectList("名称空间.sqlID");
 * 释放资源
 * Mapper代理
 * 概述：简化MyBatis操作数据库
 * 使用步骤
 * 1、定义与SQL映射文件同名的Mapper接口，并且将Mapper接口和SQL映射文件放置在同一目录下
 * 2、设置SQL映射文件的namespace属性为Mapper接口路径加名称
 * 3、在Mapper接口中定义方法，方法名就是SQL映射文件中SQL语句的id，并保持参数类型和返回值类型一致
 * 4、通过SqlSession的getMapper方法获取Mapper接口的代理对象
 * 调用对应方法完成sql的执行
 * 注意：如果Mapper接口名称和SQL映射文件名称相同，并在同一目录下，则可以使用包扫描的方式简化SQL映射文件的加载
* */

public class testDemo {
    public static void main(String[] args) throws IOException {
        //获取mybatis的核心配置文件，获取SqlSessionFactory对象
        String resource = "mybatis-config.xml";
        InputStream inputStream = Resources.getResourceAsStream(resource);
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);

        //获取对应的SqlSession对象，执行SQL
        SqlSession sqlSession = sqlSessionFactory.openSession();
//        //执行sql
//        List<User> users = sqlSession.selectList("user.selectAllUser");
        //使用Mapper代理方式执行SQL
        UserMapper mapper = sqlSession.getMapper(UserMapper.class);
        List<User> users = mapper.selectAllUser();

        System.out.println(users);
        //释放资源
        sqlSession.close();
    }
}
