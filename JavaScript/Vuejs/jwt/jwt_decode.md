[TOC]

### [1] jwt-decode

npm install: `npm install jwt-decode --save`


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

<br>

### [2] jsonwebtoken

npm install: `npm install jsonwebtoken --save`

```js

import JsonWebToken from 'jsonwebtoken'

var token = 'eyJ0eXAiO.../// jwt token';

const jwtDecode = JsonWebToken.decode(token)
console.log(decoded);

/* prints:
 * { foo: "bar",
 *   exp: 1393286893,
 *   iat: 1393268893  }
 */
```















