# Exercise 0 – Understanding HTTP vs HTTPS

## 1. Differences Between HTTP and HTTPS

- **HTTP** (HyperText Transfer Protocol) is the protocol used to send data across the web. It transfers data in plain text, meaning it can be intercepted by attackers.
- **HTTPS** (HTTP Secure) adds a layer of encryption using **TLS (formerly SSL)**. It ensures that data sent between client and server is encrypted and that the server is authenticated.

**Quick Comparison**:

| Protocol | Secure? | Default Port | Common Use Case                |
|----------|---------|--------------|--------------------------------|
| HTTP     | ❌ No    | 80           | Public/static websites         |
| HTTPS    | ✅ Yes   | 443          | Login forms, payments, APIs    |

> Example URLs:
> - `http://example.com` → not secure  
> - `https://example.com` → encrypted and verified

---

## 2. Structure of an HTTP Request and Response

### 🔸 HTTP Request (Client → Server)
A typical HTTP request includes:

1. **Request Line** – Method + Path + HTTP Version  
   Example: `GET /users HTTP/1.1`
2. **Headers** – Key-value pairs with extra info  
   Example: `User-Agent`, `Content-Type`, `Authorization`
3. **Blank Line** – Separates headers from body
4. **Body** *(optional)* – Data sent to the server (e.g. JSON, form fields)

**Example**:
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json

{
"email": "user@example.com",
"password": "secret123"
}

markdown
Copier
Modifier

### 🔹 HTTP Response (Server → Client)
A typical HTTP response includes:

1. **Status Line** – HTTP version + status code + status text  
   Example: `HTTP/1.1 200 OK`
2. **Headers** – Info about the response  
   Example: `Content-Type`, `Set-Cookie`, `Content-Length`
3. **Blank Line**
4. **Body** – Content returned by the server (e.g. HTML, JSON)

**Example**:
HTTP/1.1 404 Not Found
Content-Type: text/html

<h1>Page Not Found</h1> ```