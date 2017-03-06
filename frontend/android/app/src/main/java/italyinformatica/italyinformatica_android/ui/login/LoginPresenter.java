package italyinformatica.italyinformatica_android.ui.login;

import android.util.Log;

import com.androidnetworking.error.ANError;

import javax.inject.Inject;

import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import italyinformatica.italyinformatica_android.data.DataManager;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequest;
import italyinformatica.italyinformatica_android.data.network.model.LoginRequestVerification;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponse;
import italyinformatica.italyinformatica_android.data.network.model.LoginResponseVerification;
import italyinformatica.italyinformatica_android.ui.base.BasePresenter;

public class LoginPresenter<V extends LoginContract.View> extends BasePresenter<V> implements LoginContract.Presenter<V> {

    @Inject
    public LoginPresenter(CompositeDisposable compositeDisposable, DataManager dataManager) {
        super(compositeDisposable, dataManager);
    }

    @Override
    public void onLoginClick(String user, String pass) {
        if (user == null || user.isEmpty()) {
            getView().onError();
            return;
        }
        if (pass == null || pass.isEmpty()) {
            getView().onError();
            return;
        }

        getCompositeDisposable().add(getDataManager()
                .doServerLogin(new LoginRequest(user, pass))
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<LoginResponse>() {
                    @Override
                    public void accept(@NonNull LoginResponse loginResponse) throws Exception {
                        Log.d("token", loginResponse.getToken());
                        getView().onConfirmedLogin(loginResponse.getToken());
                        loginVerification(loginResponse.getToken());
                    }
                }, new Consumer<Throwable>() {
                    @Override
                    public void accept(@NonNull Throwable throwable) throws Exception {
                        if (throwable instanceof ANError) {
                            getView().onLoginError(((ANError) throwable).getErrorBody());
                        }
                    }
                }));
    }

    private void loginVerification(final String token) {
        getCompositeDisposable().add(getDataManager()
                .doServerLoginVerification(new LoginRequestVerification(token))
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<LoginResponseVerification>() {
                    @Override
                    public void accept(@NonNull LoginResponseVerification loginResponseVerification) throws Exception {
                        Log.d("token verification: ", loginResponseVerification.getToken());
                        if (token.equals(loginResponseVerification.getToken())) {
                            getView().onConfirmedLoginVerification(token);
                            getDataManager().setToken(token);
                        }
                        else {
                            getView().onLoginVerificationError("Tokens don't match!");
                        }
                    }
                }, new Consumer<Throwable>() {
                    @Override
                    public void accept(@NonNull Throwable throwable) throws Exception {
                        if (throwable instanceof ANError) {
                            getView().onLoginVerificationError(((ANError) throwable).getErrorBody());
                        }
                    }
                }));
    }

}
