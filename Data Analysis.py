import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

df = pd.read_csv('Final_data.csv')

# Display basic information about the dataset
print("First 5 rows of the dataset:")
print(df.head())    
print('=' * 50)
print("\nName of Columns in the dataset:")
print(df.columns)
print('=' * 50)
print("\nDataset Information:")
print(df.info())
print('=' * 50)
print("\nStatistical Summary:")
print(df.describe())   
print('=' * 50) 
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
print('=' * 50)
print("\nUnique Values in Each Column:")
print(df.nunique())    
print('=' * 50)

# Gender Characteristics
print("\nGENDER CHARACTERISTICS")
genders = df['Gender'].unique()
for gender in genders:
    gender_data = df[df['Gender'] == gender]
    age_gender = gender_data['Age'].mean()
    weight_gender = gender_data['Weight (kg)'].mean()
    height_gender = gender_data['Height (m)'].mean()
    workout_type_gender= gender_data['Workout'].nunique()
    target_muscle_gender = gender_data['Target Muscle Group'].value_counts()
    burned_calories_gender = gender_data['Burns_Calories_Bin'].value_counts()
    bmi_gender = gender_data['BMI'].mean()
    difficulty_level_gender = gender_data['Difficulty Level'].value_counts()
    water_intake_gender = gender_data['Water_Intake (liters)'].mean()
    diet_type_gender = gender_data['diet_type'].value_counts()
     

    print(f"\nGender: {gender.upper()}")
    print(f"Average Age: {age_gender:.1f}")
    print(f"Average Weight: {weight_gender:.1f} kg")
    print(f"Average Height: {height_gender:.1f} m")
    print(f"Average BMI: {bmi_gender:.1f}")
    print(f'Average Water Intake: {water_intake_gender:.1f} liters')
    print(f'Fat Percentage: {gender_data["Fat_Percentage"].mean():.1f}%')
    print('-'*30)
    print('Difficulty Level: ', gender_data["Difficulty Level"].value_counts().head(1).index[0])
    print('Most Popular Workout Type: ', gender_data["Workout"].value_counts().head(1).index[0])
    print('Most Popular Target Muscle Group: ', gender_data["Target Muscle Group"].value_counts().head(1).index[0])
    print('Burn Calories Level: ', gender_data["Burns_Calories_Bin"].value_counts().head(1).index[0])
    print('Most Common Diet Type: ', diet_type_gender.head(1).index[0])
   
    
print('='*50)


# Age Group Characteristics
age_bins = [0, 29, 39, 49, 59, 150]
age_labels = [
    "Up to 29 years",
    "30-39 years",
    "40-49 years",
    "50-59 years",
    "60+ years"
  ]
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=True)

print("\nAGE GROUP CHARACTERISTICS")
for group in age_labels:
    age_group_data = df[df['Age Group'] == group]
    if not age_group_data.empty:
        print(f"\nAge Group: {group.upper()} ")
    print(f"Average BMI: {age_group_data['BMI'].mean():.1f}")
    print(f"Average Carbs Intake: {age_group_data['Carbs'].mean():.1f}g")
    print(f"Average Proteins Intake: {age_group_data['Proteins'].mean():.1f}g")
    print(f"Average Fats Intake: {age_group_data['Fats'].mean():.1f}g")
    print(f"Average Calories Burned: {age_group_data['Calories_Burned'].mean():.1f}Kcal")
    print(f'Fat Percentage: {age_group_data["Fat_Percentage"].mean().round(1)}%')
    print(f"Average Meals Frequency: {age_group_data['Daily meals frequency'].mean():.0f}")

    

print('='*50)

# Configuração da página
st.set_page_config(
    page_title="Lifestyle Data Dashboard",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("💪 Lifestyle Data Dashboard")
st.markdown("---")

# Carregando os dados
@st.cache_data
def load_data():
    df = pd.read_csv('Final_data.csv', header=None)
    
    # Criando as faixas etárias
    age_bins = [0, 29, 39, 49, 59, 150]
    age_labels = [
        "Up to 29 years",
        "30-39 years",
        "40-49 years",
        "50-59 years",
        "60+ years"
    ]
    df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=True)
    
    return df

try:
    df = load_data()
    
    # Sidebar para filtros
    st.sidebar.header("🔍 Filters")
    
    # Filtro de gênero
    genders = ['Todos'] + list(df['Gender'].unique())
    selected_gender = st.sidebar.selectbox("Select Gender:", genders)
    
    # Filtro de faixa etária
    age_groups = ['Todos'] + list(df['Age Group'].dropna().unique())
    selected_age_group = st.sidebar.selectbox("Select Age Group:", age_groups)
    
    # Filtro de tipo de dieta
    diet_types = ['Todos'] + list(df['diet_type'].unique())
    selected_diet = st.sidebar.selectbox("Select Diet Type:", diet_types)

    # Aplicando filtros
    filtered_df = df.copy()
    
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    
    if selected_age_group != 'All':
        filtered_df = filtered_df[filtered_df['Age Group'] == selected_age_group]

    if selected_diet != 'All':
        filtered_df = filtered_df[filtered_df['diet_type'] == selected_diet]
    
    # Métricas gerais
    st.header("📊 General Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Records", len(filtered_df))
    
    with col2:
        st.metric("Average Age", f"{filtered_df['Age'].mean():.1f} years")
    
    with col3:
        st.metric("Average BMI", f"{filtered_df['BMI'].mean():.1f}")

    with col4:
        st.metric("Average Calories Burned", f"{filtered_df['Calories_Burned'].mean():.0f} kcal")

    with col5:
        st.metric("Average Fat Percentage", f"{filtered_df['Fat_Percentage'].mean():.1f}%")

    st.markdown("---")
    
    # Seção: Características por Gênero
    st.header("👥 Characteristics by Gender")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras: Média de IMC por gênero
        gender_bmi = filtered_df.groupby('Gender')['BMI'].mean().reset_index()
        fig1 = px.bar(
            gender_bmi,
            x='Gender',
            y='BMI',
            title='Average BMI by Gender',
            color='Gender',
            color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'},
            text_auto='.1f'
        )
        fig1.update_layout(showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Gráfico de barras: Calorias queimadas por gênero
        gender_calories = filtered_df.groupby('Gender')['Calories_Burned'].mean().reset_index()
        fig2 = px.bar(
            gender_calories,
            x='Gender',
            y='Calories_Burned',
            title='Average Calories Burned by Gender',
            color='Gender',
            color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'},
            text_auto='.0f'
        )
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Gráfico de pizza: Distribuição de tipos de treino por gênero
        workout_gender = filtered_df.groupby(['Gender', 'Workout']).size().reset_index(name='count')
        fig3 = px.sunburst(
            workout_gender,
            path=['Gender', 'Workout'],
            values='count',
            title='Distribution of Workout Types by Gender',
            color='Gender',
            color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'}
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with col4:
        # Gráfico de barras: Ingestão média de água por gênero
        gender_water = filtered_df.groupby('Gender')['Water_Intake (liters)'].mean().reset_index()
        fig4 = px.bar(
            gender_water,
            x='Gender',
            y='Water_Intake (liters)',
            title='Average Water Intake by Gender',
            color='Gender',
            color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'},
            text_auto='.2f'
        )
        fig4.update_layout(showlegend=False)
        st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("---")
    
    # Seção: Características por Faixa Etária
    st.header("📅 Characteristics by Age Group")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de linhas: IMC médio por faixa etária
        age_bmi = filtered_df.groupby('Age Group')['BMI'].mean().reset_index()
        fig5 = px.line(
            age_bmi,
            x='Age Group',
            y='BMI',
            title='Average BMI by Age Group',
            markers=True,
            line_shape='spline'
        )
        fig5.update_traces(line_color='#2ca02c', marker=dict(size=10))
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        # Gráfico de barras: Calorias queimadas por faixa etária
        age_calories = filtered_df.groupby('Age Group')['Calories_Burned'].mean().reset_index()
        fig6 = px.bar(
            age_calories,
            x='Age Group',
            y='Calories_Burned',
            title='Average Calories Burned by Age Group',
            color='Calories_Burned',
            color_continuous_scale='Viridis',
            text_auto='.0f'
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Gráfico de barras agrupadas: Macronutrientes por faixa etária
        age_macros = filtered_df.groupby('Age Group')[['Carbs', 'Proteins', 'Fats']].mean().reset_index()
        fig7 = go.Figure()
        fig7.add_trace(go.Bar(name='Carboidratos', x=age_macros['Age Group'], y=age_macros['Carbs'], marker_color='#8c564b'))
        fig7.add_trace(go.Bar(name='Proteínas', x=age_macros['Age Group'], y=age_macros['Proteins'], marker_color='#e377c2'))
        fig7.add_trace(go.Bar(name='Gorduras', x=age_macros['Age Group'], y=age_macros['Fats'], marker_color='#7f7f7f'))
        fig7.update_layout(
            title='Average Macronutrient Intake by Age Group',
            xaxis_title='Age Group',
            yaxis_title='Grams (g)',
            barmode='group'
        )
        st.plotly_chart(fig7, use_container_width=True)
    
    with col4:
        # Gráfico de linhas: Percentual de gordura por faixa etária
        age_fat = filtered_df.groupby('Age Group')['Fat_Percentage'].mean().reset_index()
        fig8 = px.line(
            age_fat,
            x='Age Group',
            y='Fat_Percentage',
            title='Average Fat Percentage by Age Group',
            markers=True,
            line_shape='spline'
        )
        fig8.update_traces(line_color='#d62728', marker=dict(size=10))
        st.plotly_chart(fig8, use_container_width=True)
    
    st.markdown("---")
    
    # Seção: Análise de Dieta e Treino
    st.header("🥗 Diet and Workout Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pizza: Distribuição de tipos de dieta
        diet_dist = filtered_df['diet_type'].value_counts().reset_index()
        diet_dist.columns = ['diet_type', 'count']
        fig9 = px.pie(
            diet_dist,
            names='diet_type',
            values='count',
            title='Distribution of Diet Types',
            hole=0.4
        )
        st.plotly_chart(fig9, use_container_width=True)
    
    with col2:
        # Gráfico de pizza: Distribuição de níveis de dificuldade
        difficulty_dist = filtered_df['Difficulty Level'].value_counts().reset_index()
        difficulty_dist.columns = ['Difficulty Level', 'count']
        fig10 = px.pie(
            difficulty_dist,
            names='Difficulty Level',
            values='count',
            title='Distribution of Difficulty Levels',
            hole=0.4
        )
        st.plotly_chart(fig10, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Gráfico de barras: Grupos musculares mais trabalhados
        muscle_groups = filtered_df['Target Muscle Group'].value_counts().head(10).reset_index()
        muscle_groups.columns = ['Target Muscle Group', 'count']
        fig11 = px.bar(
            muscle_groups,
            x='count',
            y='Target Muscle Group',
            orientation='h',
            title='Top 10 Target Muscle Groups Worked',
            color='count',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig11, use_container_width=True)
    
    with col4:
        # Gráfico de barras: Tipos de treino mais populares
        workout_types = filtered_df['Workout'].value_counts().reset_index()
        workout_types.columns = ['Workout', 'count']
        fig12 = px.bar(
            workout_types,
            x='Workout',
            y='count',
            title='Most Popular Workout Types',
            color='count',
            color_continuous_scale='Greens',
            text_auto=True
        )
        st.plotly_chart(fig12, use_container_width=True)
    
    st.markdown("---")
    
    # Seção: Correlações e Análises Avançadas
    st.header("🔬 Correlations and Advanced Analyses")

    col1, col2 = st.columns(2)
    
    with col1:
        # Scatter plot: IMC vs Calorias Queimadas
        fig13 = px.scatter(
            filtered_df,
            x='BMI',
            y='Calories_Burned',
            color='Gender',
            title='Relationship between BMI and Calories Burned',
            trendline='ols',
            hover_data=['Age', 'Workout'],
            color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'}
        )
        st.plotly_chart(fig13, use_container_width=True)
    
    with col2:
        # Scatter plot: Ingestão de Água vs Percentual de Gordura
        fig14 = px.scatter(
            filtered_df,
            x='Water_Intake (liters)',
            y='Fat_Percentage',
            color='Gender',
            title='Relationship between Water Intake and Fat Percentage',
            trendline='ols',
            hover_data=['Age', 'BMI'],
            color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'}
        )
        st.plotly_chart(fig14, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Box plot: Distribuição de calorias queimadas por tipo de treino
        fig15 = px.box(
            filtered_df,
            x='Workout',
            y='Calories_Burned',
            color='Workout',
            title='Distribution of Calories Burned by Workout Type'
        )
        st.plotly_chart(fig15, use_container_width=True)
    
    with col4:
        # Violin plot: Distribuição de IMC por tipo de dieta
        fig16 = px.violin(
            filtered_df,
            x='diet_type',
            y='BMI',
            color='diet_type',
            title='Distribution of BMI by Diet Type',
            box=True
        )
        st.plotly_chart(fig16, use_container_width=True)
    
    st.markdown("---")
    
    # Seção: Tabela de Dados Filtrados
    st.header("📋 Filtered Data")
    
    # Seletor de colunas para exibir
    all_columns = list(filtered_df.columns)
    default_columns = ['Age', 'Gender', 'BMI', 'Workout', 'Calories_Burned', 'diet_type', 'Difficulty Level']
    selected_columns = st.multiselect(
        "Select the columns to display:",
        all_columns,
        default=default_columns
    )
    
    if selected_columns:
        st.dataframe(filtered_df[selected_columns], use_container_width=True)
    else:
        st.warning("Please select at least one column to display.")
    
    # Estatísticas descritivas
    if st.checkbox("Show Descriptive Statistics"):
        st.subheader("Descriptive Statistics of Filtered Data")
        st.dataframe(filtered_df.describe(), use_container_width=True)

except FileNotFoundError:
    st.error("❌ Error: 'Final_data.csv' file not found. Please ensure the file is in the same directory as the script.")
except Exception as e:
    st.error(f"❌ Error loading data: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Dashboard developed with Streamlit 🚀</p>
        <p>Data: Lifestyle Data Analysis</p>
    </div>
    """,
    unsafe_allow_html=True
)
