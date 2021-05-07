import java.io.IOException;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class RestJson {
    public static void main(String[] args) throws IOException {
        
        String url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=130010";
        String json_data = "";
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(url).build();

        //get json data with http request
        try (Response response = client.newCall(request).execute()) {
          json_data = response.body().string();
          //debug print
          //System.out.println(json_data);
        } catch ( IOException e) {
          System.out.println("request error:");
        }
        
        //parse json data
        JSONParser parser = new JSONParser();
        try {
          JSONObject json = (JSONObject) parser.parse(json_data);
          System.out.println("forecasts=" + json.get("forecasts"));
        } catch ( ParseException e) {
          System.out.println(e.toString() + "parse error:");
        }
    }
}
