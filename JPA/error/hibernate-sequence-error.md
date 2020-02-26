https://stackoverflow.com/questions/32968527/hibernate-sequence-doesnt-exist



---

### 1 @GeneratedValue

```
@GeneratedValue(strategy=GenerationType.AUTO) 를
@GeneratedValue(strategy=GenerationType.IDENTITY) 로 변경
```

---

### 2 JPA hibernate property 수정

> org.hibernate.dialect.MySQLDialect 설정

```java
private Properties getHibernateProperties() {
    Properties properties = new Properties();
    properties.put("hibernate.show_sql", "true");
    properties.put("hibernate.dialect", "org.hibernate.dialect.MySQLDialect");
    properties.put("hibernate.id.new_generator_mappings","false");
    return properties;
}
```

```java
@Bean
public LocalContainerEntityManagerFactoryBean entityManagerFactory() {

    LocalContainerEntityManagerFactoryBean entityManagerFactoryBean = new LocalContainerEntityManagerFactoryBean();
    entityManagerFactoryBean.setDataSource(dataSource());
    entityManagerFactoryBean.setPackagesToScan("your package");
    JpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();
    entityManagerFactoryBean.setJpaVendorAdapter(vendorAdapter);

    Map<String, Object> jpaPropertyMap = entityManagerFactoryBean.getJpaPropertyMap();
    jpaPropertyMap.put(AvailableSettings.DEFAULT_BATCH_FETCH_SIZE, 1000);
    jpaPropertyMap.put(AvailableSettings.JDBC_TIME_ZONE, "UTC");
    jpaPropertyMap.put(AvailableSettings.GLOBALLY_QUOTED_IDENTIFIERS, true);
    jpaPropertyMap.put(AvailableSettings.STATEMENT_BATCH_SIZE, 100);
    jpaPropertyMap.put(AvailableSettings.ORDER_INSERTS, true);
    jpaPropertyMap.put(AvailableSettings.DIALECT, "org.hibernate.dialect.MySQLDialect");
    //        jpaPropertyMap.put(AvailableSettings.USE_NEW_ID_GENERATOR_MAPPINGS, false);

    return entityManagerFactoryBean;
}
```



