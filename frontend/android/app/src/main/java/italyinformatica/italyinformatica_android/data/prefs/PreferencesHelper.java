package italyinformatica.italyinformatica_android.data.prefs;

public interface PreferencesHelper {

    /**
     * Stores access token in SharedPreferences ("INFO.xml" file).
     * @param token
     */
    void setToken(String token);

    /**
     * Returns access token stored in SharedPreferences.
     * @return String
     */
    String getToken();

    /**
     * Returns value of property stored in res/raw/config.properties
     * @param name      es: "BASE_URL". Name of the property
     * @return          String
     */
    String getConfigValue(String name);

}
