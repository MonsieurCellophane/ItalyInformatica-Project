package italyinformatica.italyinformatica_android.di.module;

import android.app.Activity;
import android.content.Context;

import dagger.Module;
import dagger.Provides;
import io.reactivex.disposables.CompositeDisposable;
import italyinformatica.italyinformatica_android.di.ActivityContext;
import italyinformatica.italyinformatica_android.di.PerActivity;
import italyinformatica.italyinformatica_android.ui.login.LoginContract;
import italyinformatica.italyinformatica_android.ui.login.LoginPresenter;
import italyinformatica.italyinformatica_android.ui.main.MainContract;
import italyinformatica.italyinformatica_android.ui.main.MainPresenter;

@Module
public class ActivityModule {

    private Activity mActivity;

    public ActivityModule(Activity activity) {
        mActivity = activity;
    }

    @Provides
    @ActivityContext
    Context provideContext() {
        return mActivity;
    }

    @Provides
    Activity provideActivity() {
        return mActivity;
    }

    @Provides
    CompositeDisposable provideCompositeDisposable() {
        return new CompositeDisposable();
    }

    @Provides
    @PerActivity
    MainContract.Presenter<MainContract.View> provideMainPresenter(MainPresenter<MainContract.View> presenter) {
        return presenter;
    }

    @Provides
    @PerActivity
    LoginContract.Presenter<LoginContract.View> provideLoginPresenter(LoginPresenter<LoginContract.View> presenter) {
        return presenter;
    }
}
