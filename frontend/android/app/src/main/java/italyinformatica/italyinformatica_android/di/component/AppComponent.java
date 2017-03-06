package italyinformatica.italyinformatica_android.di.component;

import android.app.Application;
import android.content.Context;

import javax.inject.Singleton;

import dagger.Component;
import italyinformatica.italyinformatica_android.IIPApp;
import italyinformatica.italyinformatica_android.data.DataManager;
import italyinformatica.italyinformatica_android.di.AppContext;
import italyinformatica.italyinformatica_android.di.module.AppModule;

@Singleton
@Component(modules = AppModule.class)
public interface AppComponent {

    void inject(IIPApp app);

    @AppContext
    Context context();

    Application application();

    DataManager getDataManager();

}
