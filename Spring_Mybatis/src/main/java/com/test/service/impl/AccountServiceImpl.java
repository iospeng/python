package com.test.service.impl;

import com.test.dao.AccountDao;
import com.test.domain.Account;
import com.test.service.AccountService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountServiceImpl implements AccountService {
    @Autowired
    private AccountDao accountDao;
    @Override
    public Account findById(Integer id) {
        return accountDao.findById(id);
    }
}
