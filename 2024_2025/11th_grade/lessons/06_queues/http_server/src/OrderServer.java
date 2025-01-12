import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.util.Map;

class Order {
    int number;
    String details;
}

public class OrderServer implements HttpHandler {
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        if ("POST".equals(exchange.getRequestMethod())) {
            System.out.println("Received request: " + exchange.getRequestURI());
            InputStream requestBodyStream = exchange.getRequestBody();
            String requestBody = new String(requestBodyStream.readAllBytes(), StandardCharsets.UTF_8);
            var g = new Gson();

            var order =  g.fromJson(requestBody, Order.class);
            String response = "Thank you";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();

            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                System.out.println("not supposed to happen");
            }
            System.out.println("Number: " + order.number);
            System.out.println("Details:" + order.details);


        } else {
            exchange.sendResponseHeaders(405, -1); // Method Not Allowed
        }
    }
}
