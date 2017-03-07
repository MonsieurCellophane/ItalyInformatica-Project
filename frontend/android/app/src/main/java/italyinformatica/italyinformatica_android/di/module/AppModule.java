package italyinformatica.italyinformatica_android.di.module;

import android.app.Application;
import android.content.Context;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;
import italyinformatica.italyinformatica_android.data.DataManager;
import italyinformatica.italyinformatica_android.data.DataManagerImpl;
import italyinformatica.italyinformatica_android.data.network.ApiHelper;
import italyinformatica.italyinformatica_android.data.network.ApiHelperImpl;
import italyinformatica.italyinformatica_android.data.prefs.PreferencesHelper;
import italyinformatica.italyinformatica_android.data.prefs.PreferencesHelperImpl;
import italyinformatica.italyinformatica_android.di.AppContext;

@Module
public class AppModule {

    private final Application mApplication;

    public AppModule(Application application) {
        mApplication = application;
    }

    @Provides
    @AppContext
    Context provideContext() {
        return mApplication;
    }

    @Provides
    Application provideApplication() {
        return mApplication;
    }

    @Provides
    @Singleton
    DataManager provideDataManager(DataManagerImpl dataManagerImpl) {
        return dataManagerImpl;
    }

    @Provides
    @Singleton
    PreferencesHelper providePreferencesHelper(PreferencesHelperImpl preferencesHelperImpl) {
        return preferencesHelperImpl;
    }

    @Provides
    @Singleton
    ApiHelper provideApiHelper(ApiHelperImpl apiHelperImpl) {
        return apiHelperImpl;
    }

}
