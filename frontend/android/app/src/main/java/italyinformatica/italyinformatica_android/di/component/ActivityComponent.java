package italyinformatica.italyinformatica_android.di.component;

import dagger.Component;
import italyinformatica.italyinformatica_android.di.PerActivity;
import italyinformatica.italyinformatica_android.di.module.ActivityModule;
import italyinformatica.italyinformatica_android.ui.base.BaseActivity;
import italyinformatica.italyinformatica_android.ui.login.LoginActivity;
import italyinformatica.italyinformatica_android.ui.main.MainActivity;

@PerActivity
@Component(dependencies = AppComponent.class, modules = ActivityModule.class)
public interface ActivityComponent {

    void inject(MainActivity activity);

    void inject(LoginActivity activity);

}
