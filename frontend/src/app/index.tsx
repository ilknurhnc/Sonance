import { useEffect, useState } from "react";
import { ActivityIndicator, SafeAreaView, StyleSheet, Text, View } from "react-native";

const API_BASE_URL = "http://localhost:8000";

export default function HomeScreen() {
  const [status, setStatus] = useState<string>("checking");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    checkBackendHealth();
  }, []);

  async function checkBackendHealth() {
    try {
      const response = await fetch(`${API_BASE_URL}/health`);
      const data = await response.json();

      setStatus(data.status);
    } catch (err) {
      console.log(err);
      setError(String(err));
    }
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.title}>Sonance</Text>
        <Text style={styles.subtitle}>Every playlist has a personality.</Text>

        {error ? (
          <Text style={styles.error}>{error}</Text>
        ) : status === "checking" ? (
          <ActivityIndicator />
        ) : (
          <Text style={styles.success}>Backend status: {status}</Text>
        )}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#111111",
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
  },
  card: {
    width: "100%",
    padding: 24,
    borderRadius: 24,
    backgroundColor: "#1C1C1C",
  },
  title: {
    fontSize: 36,
    fontWeight: "700",
    color: "#FFFFFF",
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: "#BDBDBD",
    marginBottom: 24,
  },
  success: {
    fontSize: 16,
    color: "#8CE99A",
  },
  error: {
    fontSize: 16,
    color: "#FF8787",
  },
});