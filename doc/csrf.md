#### 1.get无副作用


#### 2.post 提交请求

```html
GET 请求不需要 CSRF 认证，POST 请求需要正确认证才能得到正确的返回结果。一般在POST表单中加入 {% csrf_token %}
<input type="" name="csrfmiddlewaretoken" value="x1TbrloEBHG6YspLC0mYEZM03KU4zzVrRIDoTYHHIgk81BetebFpDDkN6cLgbqDY">
```

####

