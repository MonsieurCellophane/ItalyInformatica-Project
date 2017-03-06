package italyinformatica.italyinformatica_android.data.prefs;

import android.content.Context;
import android.content.SharedPreferences;

import javax.inject.Inject;
import javax.inject.Singleton;

import italyinformatica.italyinformatica_android.di.AppContext;

@Singleton
public class PreferencesHelperImpl implements PreferencesHelper {

    private static final String PREF_KEY_ACCESS_TOKEN = "PREF_KEY_ACCESS_TOKEN";

    private final SharedPreferences mPrefs;

    @Inject
    public PreferencesHelperImpl(@AppContext Context context) {
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
}
