package italyinformatica.italyinformatica_android.data.network;

import android.content.Context;

import com.rx2androidnetworking.Rx2AndroidNetworking;

import javax.inject.Inject;
import javax.inject.Singleton;

import io.reactivex.Observable;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequest;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequestVerification;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponse;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponseVerification;
import italyinformatica.italyinformatica_android.di.AppContext;

@Singleton
public class ApiHelperImpl implements ApiHelper {

    private final Context mContext;

    @Inject
    public ApiHelperImpl(@AppContext Context context) {
        mContext = context;
    }

    @Override
    public Observable<LoginResponse> doServerLogin(LoginRequest request) {
        return Rx2AndroidNetworking.post(ApiEndpoint.API_AUTH_TOKEN)
                .addBodyParameter(request)
                .build()
                .getObjectObservable(LoginResponse.class);
    }

    @Override
    public Observable<LoginResponseVerification> doServerLoginVerification(LoginRequestVerification requestVerification) {
        return Rx2AndroidNetworking.post(ApiEndpoint.API_AUTH_VERIFY)
                .addBodyParameter(requestVerification)
                .build()
                .getObjectObservable(LoginResponseVerification.class);
    }
}
