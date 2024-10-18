import { SplitView } from '@/components/SplitView';
import { ThemedSafeAreaView } from '@/components/ThemedSafeAreaView';
import { ThemedView } from '@/components/ThemedView';
import { Colors } from '@/constants/Colors';
import { useLibraryWallpapers, useLikedWallpapers, useSuggestedWallpapers, } from '@/hooks/useWallpapers';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import {  useColorScheme } from 'react-native';
import { StyleSheet } from 'react-native';


const Tab = createMaterialTopTabNavigator();

export default function ForYou() {
  const theme = useColorScheme() ?? 'light';

  return (
    <ThemedSafeAreaView style={styles.container}>
        <Tab.Navigator style={{
            flex: 1,
        }} screenOptions={{
            tabBarActiveTintColor: Colors[theme].tint,
            tabBarStyle: {
                backgroundColor: Colors[theme].background,
            }, 
            tabBarIndicatorStyle: {
                backgroundColor: Colors[theme].indicator,
                height: 5
            }
        }}>
            <Tab.Screen name="Library" component={LibraryScreen} />
            <Tab.Screen name="Liked" component={LikedScreen} />
            <Tab.Screen name="Suggested" component={SuggestedScreen} />
        </Tab.Navigator>
    </ThemedSafeAreaView>
  );
}

function LibraryScreen() {
    const walletpapers = useLibraryWallpapers();

    return <ThemedView style={styles.container}>
        <SplitView wallpapers={walletpapers} />
    </ThemedView>
}

function LikedScreen() {
    const walletpapers = useLikedWallpapers();

    return <ThemedView style={styles.container}>
        <SplitView wallpapers={walletpapers} />
    </ThemedView>
}

function SuggestedScreen() {
    const walletpapers = useSuggestedWallpapers();

    return <ThemedView style={styles.container}>
        <SplitView wallpapers={walletpapers} />
    </ThemedView>
}
 
const styles = StyleSheet.create({
    container: {
        flex: 1
    }
})