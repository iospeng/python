package com.test.domain;

import java.io.Serializable;

public class Account implements Serializable {
    private Integer id;         // 店铺ID
    private Integer user_id;    // 商家ID
    private String user_name;   // 商家名称
    private String store_name;  // 店铺名称
    private String store_address;    // 店铺地址

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getUser_id() {
        return user_id;
    }

    public void setUser_id(Integer user_id) {
        this.user_id = user_id;
    }

    public String getUser_name() {
        return user_name;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }

    public String getStore_name() {
        return store_name;
    }

    public void setStore_name(String store_name) {
        this.store_name = store_name;
    }

    public String getStore_address() {
        return store_address;
    }

    public void setStore_address(String store_address) {
        this.store_address = store_address;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", user_id=" + user_id +
                ", user_name='" + user_name + '\'' +
                ", store_name='" + store_name + '\'' +
                ", store_address='" + store_address + '\'' +
                '}';
    }
}
