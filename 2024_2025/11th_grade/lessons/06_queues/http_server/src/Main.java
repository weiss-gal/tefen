import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

import com.google.gson.Gson;

class SimpleHttpHandler implements HttpHandler {
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        if ("POST".equals(exchange.getRequestMethod())) {
            System.out.println("Received request: " + exchange.getRequestURI());
            InputStream requestBodyStream = exchange.getRequestBody();
            String requestBody = new String(requestBodyStream.readAllBytes(), StandardCharsets.UTF_8);
            System.out.println("Request body:\n" + requestBody);

            String response = "Thank you";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        } else if ("GET".equals(exchange.getRequestMethod())) {
            String response = "Hello";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        } else {
            exchange.sendResponseHeaders(405, -1); // Method Not Allowed
        }

    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("Server is running");
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/send", new SimpleHttpHandler());

        //Executor executor = Executors.newFixedThreadPool(10); // Pool size of 10 threads
        server.setExecutor(null); // creates a default executor
        server.start();
    }
}