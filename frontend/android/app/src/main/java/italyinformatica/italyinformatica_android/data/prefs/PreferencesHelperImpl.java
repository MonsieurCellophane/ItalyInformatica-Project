package italyinformatica.italyinformatica_android.data.prefs;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.Resources;
import android.util.Log;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import javax.inject.Inject;
import javax.inject.Singleton;

import italyinformatica.italyinformatica_android.R;
import italyinformatica.italyinformatica_android.di.AppContext;

@Singleton
public class PreferencesHelperImpl implements PreferencesHelper {

    private static final String TAG = "PreferencesHelper";
    private static final String PREF_KEY_ACCESS_TOKEN = "PREF_KEY_ACCESS_TOKEN";

    private final Context mContext;
    private final SharedPreferences mPrefs;

    @Inject
    public PreferencesHelperImpl(@AppContext Context context) {
        mContext = context;
        mPrefs = context.getSharedPreferences("INFO", Context.MODE_PRIVATE);
    }

    @Override
    public String getToken() {
        return mPrefs.getString(PREF_KEY_ACCESS_TOKEN, null);
    }

    @Override
    public void setToken(String token) {
        mPrefs.edit().putString(PREF_KEY_ACCESS_TOKEN, token).apply();
    }

    @Override
    public String getConfigValue(String name) {
        Resources resources = mContext.getResources();
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
}
