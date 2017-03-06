package italyinformatica.italyinformatica_android.data.network;

import io.reactivex.Observable;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequest;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequestVerification;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponse;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponseVerification;

public interface ApiHelper {

    Observable<LoginResponse> doServerLogin(LoginRequest request);

    Observable<LoginResponseVerification> doServerLoginVerification(LoginRequestVerification requestVerification);

}
