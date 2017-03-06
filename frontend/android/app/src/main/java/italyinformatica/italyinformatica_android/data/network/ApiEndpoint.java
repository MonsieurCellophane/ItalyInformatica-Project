package italyinformatica.italyinformatica_android.data.network;

public final class ApiEndpoint {

    public static final String BASE_URL = "http://localhost:8000";

    public static final String API_AUTH_TOKEN = BASE_URL + "/api/auth/token/";

    public static final String API_AUTH_VERIFY = BASE_URL + "/api/auth/verify/";

    private ApiEndpoint() {

    }

}
