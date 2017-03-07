package italyinformatica.italyinformatica_android.data.network;

import android.content.Context;
import android.content.res.Resources;
import android.util.Log;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import italyinformatica.italyinformatica_android.R;

public final class ApiEndpoint {

    public static final String TAG = "ApiEndpoint";

    private ApiEndpoint() {

    }

    private static String getConfigValue(Context context, String name) {
        Resources resources = context.getResources();
        try {
            InputStream rawResource = resources.openRawResource(R.raw.config);
            Properties properties = new Properties();
            properties.load(rawResource);
            return properties.getProperty(name);
        } catch (Resources.NotFoundException e) {
            Log.e(TAG, "Unable to find the config file. Are you sure you created res/raw/config.properties ? : " + e.getMessage());
        } catch (IOException e) {
            Log.e(TAG, "Failed to open config file.");
        }
        return null;
    }

    public static String getBaseUrl(Context context) {
        return getConfigValue(context, "BASE_URL");
    }

    public static String getApiAuthToken(Context context) {
        return getConfigValue(context, "API_AUTH_TOKEN");
    }

    public static String getApiAuthVerify(Context context) {
        return getConfigValue(context, "API_AUTH_VERIFY");
    }

}
