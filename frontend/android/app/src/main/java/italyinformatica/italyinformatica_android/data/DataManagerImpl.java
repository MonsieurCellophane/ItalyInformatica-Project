package italyinformatica.italyinformatica_android.data;

import android.content.Context;

import javax.inject.Inject;
import javax.inject.Singleton;

import io.reactivex.Observable;
import italyinformatica.italyinformatica_android.data.network.ApiHelper;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequest;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequestVerification;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponse;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponseVerification;
import italyinformatica.italyinformatica_android.data.prefs.PreferencesHelper;
import italyinformatica.italyinformatica_android.di.AppContext;

@Singleton
public class DataManagerImpl implements DataManager {

    private final Context mContext;
    private final PreferencesHelper mPreferencesHelper;
    private final ApiHelper mApiHelper;

    @Inject
    public DataManagerImpl(@AppContext Context context,
                           PreferencesHelper preferencesHelper,
                           ApiHelper apiHelper) {
        mContext = context;
        mPreferencesHelper = preferencesHelper;
        mApiHelper = apiHelper;
    }

    @Override
    public Observable<LoginResponse> doServerLogin(LoginRequest request) {
        return mApiHelper.doServerLogin(request);
    }

    @Override
    public Observable<LoginResponseVerification> doServerLoginVerification(LoginRequestVerification requestVerification) {
        return mApiHelper.doServerLoginVerification(requestVerification);
    }

    @Override
    public String getToken() {
        return mPreferencesHelper.getToken();
    }

    @Override
    public void setToken(String token) {
        mPreferencesHelper.setToken(token);
    }

}
