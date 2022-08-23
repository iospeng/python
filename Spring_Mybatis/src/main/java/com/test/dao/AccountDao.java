package com.test.dao;

import com.test.domain.Account;
import org.apache.ibatis.annotations.Select;

public interface AccountDao {
    @Select("select * from store where id = #{id}")
    Account findById(Integer id);
}
