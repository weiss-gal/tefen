import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.requests.GatewayIntent;

import javax.security.auth.login.LoginException;

class MyFirstBot extends ListenerAdapter {

    public static void main(String[] args) throws Exception {
        String token = new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("token.txt"))).trim();
        JDABuilder.createDefault(token)
                .addEventListeners(new MyFirstBot())
                .enableIntents(GatewayIntent.MESSAGE_CONTENT)
                .build();
    }

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        if (event.getAuthor().isBot()) return;

        Message message = event.getMessage();
        String content = message.getContentRaw();

        System.out.println("Message receieved: [" + content + "]");
        if (content.equalsIgnoreCase("!ping")) {
            event.getChannel().sendMessage("Pong!").queue();
        }
    }
}

