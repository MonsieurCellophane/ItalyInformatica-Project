package italyinformatica.italyinformatica_android.data.network;

import io.reactivex.Observable;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequest;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequestVerification;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponse;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponseVerification;

public interface ApiHelper {

    /**
     * Login to server. Takes a LoginRequest (username and password) and returns a
     * LoginResponse observable with access token.
     * @param request           LoginRequest object with username and password
     * @return LoginResponse    Observable with token
     */
    Observable<LoginResponse> doServerLogin(LoginRequest request);

    /**
     * Token verification call. Takes a LoginRequestVerification object with access token
     * (previously obtained), and returns a LoginResponseVerification observable with the
     * same token.
     * @param requestVerification           LoginRequestVerification object with token
     * @return LoginResponseVerification    Observable with token
     */
    Observable<LoginResponseVerification> doServerLoginVerification(LoginRequestVerification requestVerification);

}
