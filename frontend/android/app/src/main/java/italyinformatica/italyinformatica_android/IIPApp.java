package italyinformatica.italyinformatica_android;

import android.app.Application;

import italyinformatica.italyinformatica_android.di.component.AppComponent;
import italyinformatica.italyinformatica_android.di.component.DaggerAppComponent;
import italyinformatica.italyinformatica_android.di.module.AppModule;

public class IIPApp extends Application {

    private AppComponent mAppComponent;

    @Override
    public void onCreate() {
        super.onCreate();

        mAppComponent = DaggerAppComponent.builder()
                .appModule(new AppModule(this))
                .build();

        mAppComponent.inject(this);

    }

    public AppComponent getAppComponent() {
        return mAppComponent;
    }
}
