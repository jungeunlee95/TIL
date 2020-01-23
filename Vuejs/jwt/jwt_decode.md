jwt decode

### npm install
`npm install jwt-decode`


ex)
```js

import jwt_decode from 'jwt-decode'

var token = 'eyJ0eXAiO.../// jwt token';

var decoded = jwt_decode(token);
console.log(decoded);

/* prints:
 * { foo: "bar",
 *   exp: 1393286893,
 *   iat: 1393268893  }
 */

```

