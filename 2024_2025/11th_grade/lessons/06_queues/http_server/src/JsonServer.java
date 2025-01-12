import com.google.gson.reflect.TypeToken;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.util.Map;

import com.google.gson.Gson;

public class JsonServer implements HttpHandler {
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        if ("POST".equals(exchange.getRequestMethod())) {

            System.out.println("Received request: " + exchange.getRequestURI());
            InputStream requestBodyStream = exchange.getRequestBody();
            String requestBody = new String(requestBodyStream.readAllBytes(), StandardCharsets.UTF_8);
            var g = new Gson();
            Type mapType = new TypeToken<Map<String, Object>>() {}.getType();
            Map<String, Object> map =  g.fromJson(requestBody, mapType);
            for (var x : map.keySet()){
                System.out.println("Key: " + x);
                System.out.println("Value:" + map.get(x));
            }

            String response = "Thank you";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        } else {
            exchange.sendResponseHeaders(405, -1); // Method Not Allowed
        }
    }
}
